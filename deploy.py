import os
import re
import shutil
import subprocess
import tokenize
import io

GH_BRANCH = "main"

EXTENSIONS = (".kt", ".js", ".jsx", ".css", ".py")


WEB_DIR_PATH = os.path.join("app", "src", "main", "java", "com", "example", "spot", "web")

def get_current_branch():
    result = subprocess.run("git rev-parse --abbrev-ref HEAD", shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def remove_comments(text, ext):
    if ext == '.py':
        try:
            tokens = tokenize.generate_tokens(io.StringIO(text).readline)
            comments = []
            for tok in tokens:
                if tok.type == tokenize.COMMENT:
                    comments.append((tok.start[0] - 1, tok.start[1]))
            
            lines = text.splitlines(keepends=True)
            for line_idx, col_idx in reversed(comments):
                line = lines[line_idx]
                newline = "\r\n" if line.endswith("\r\n") else ("\n" if line.endswith("\n") else "")
                lines[line_idx] = line[:col_idx].rstrip() + newline
                
            return "".join(lines)
        except Exception:
            return text
    else:

        text = re.sub(r'/\*[\s\S]*?\*/', '', text)
        text = re.sub(r'(?<!:)\/\/.*', '', text)
    return text

def clean_source_files():
    src_dir = os.getcwd()
    for root, _, files in os.walk(src_dir):

        if any(part in root for part in [".git", ".gradle", "build", "app/build", "__pycache__"]):
            continue
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in EXTENSIONS:
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                cleaned_content = remove_comments(content, ext)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(cleaned_content)

def run_cmd(cmd):
    subprocess.run(cmd, shell=True, check=True)

dev_branch = get_current_branch()
if dev_branch == GH_BRANCH:
    print(f"[ОТМЕНА] Ты на ветке {GH_BRANCH}. Переключись на dev перед запуском!")
    exit(1)

try:
    print(f"1. Фиксируем изменения в рабочей ветке {dev_branch}...")
    run_cmd("git add .")
    run_cmd('git commit -m "Save dev state" --allow-empty')

    print(f"2. Скачиваем актуальное состояние с GitHub...")
    run_cmd("git fetch origin")

    print(f"3. Переключаемся на ветку {GH_BRANCH} и синхронизируем указатели...")
    run_cmd(f"git checkout -f {GH_BRANCH}")
    try:
        run_cmd(f"git reset --hard origin/{GH_BRANCH}")
    except Exception:
        pass
    
    print(f"4. Подтягиваем код из {dev_branch}...")
    run_cmd(f"git checkout {dev_branch} -- .")


    full_web_path = os.path.join(os.getcwd(), WEB_DIR_PATH)
    if os.path.exists(full_web_path):
        print("4.5. Вырезаем конфиденциальную папку web...")
        shutil.rmtree(full_web_path)

    print("5. Вырезаем комментарии из кода...")
    clean_source_files()

    print("Проверка на наличие фактических изменений...")
    check_status = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if not check_status.stdout.strip():
        print("\n[ОТМЕНА] Логических изменений нет. Код полностью совпадает с GitHub. Деплой отменен.")
        run_cmd(f"git checkout -f {dev_branch}")
        exit(0)

    print(f"6. Отправляем чистый код на GitHub...")
    run_cmd("git add .")
    run_cmd('git commit -m "Build: production release without comments" --allow-empty')

    run_cmd(f"git push -f origin {GH_BRANCH}")

    print(f"7. Возвращаемся обратно в рабочую ветку {dev_branch}...")
    run_cmd(f"git checkout -f {dev_branch}")
    print("\n[УСПЕХ] Всё готово. Локальный код на dev в порядке, на гитхабе чистый скелет без адблока!")

except Exception as e:
    print(f"\n[ОШИБКА] Косяк: {e}")
    run_cmd(f"git checkout -f {dev_branch}")