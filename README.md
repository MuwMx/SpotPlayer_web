# Spot 🎵

<p align="center">
  <strong>A premium, feature-rich Android client for music web services</strong><br>
  Built from scratch using a modern Android stack, clean architecture, and an optimized WebView core.
</p>

<p align="center">
  <img src="screenshots/player_blur.png" width="200" style="border-radius:26px;"/>
  <img src="screenshots/player_gradient.png" width="200" style="border-radius:26px;"/>
  <img src="screenshots/lyrics.png" width="200" style="border-radius:26px;"/>
</p>

<p align="center">
    <a href="https://t.me/spot_app_player" target="_blank">
        <img src="https://img.shields.io/badge/Telegram-Official%20Channel-26A6E4?style=for-the-badge&logo=telegram" alt="Telegram Channel">
    </a>
    <img src="https://img.shields.io/badge/Android-11%2B-green?style=for-the-badge&logo=android" alt="Android 11+">
    <img src="https://img.shields.io/badge/Kotlin-100%25-purple?style=for-the-badge&logo=kotlin" alt="Kotlin">
</p>

---

## ‼️ Disclaimer
- This is a standalone, third-party application. This repository serves strictly as a project passport and architecture showcase. No source code or build support is provided here. All binary updates are distributed exclusively through the community channel.

---

## ✨ Features

### 🎨 Next-Gen UI/UX
- **Dynamic Monet Engine** — Implements Google’s Material You advanced color extraction, blending the entire UI theme with the current track's artwork.
- **Dual Presentation Themes** — Switch instantly between an ultra-clean minimalist Gradient look and an immersive, hardware-accelerated Blur theme.
- **Edge-Faded Typography** — Canvas-based horizontal растворение (Marquee) for long titles, providing elegant layout protection without truncated text.
- **Fluid Micro-Interactions** — Spring-physics driven animations, touch-zone layout offsets, and gesture-responsive sliding sheets.

### ⚡ Smart Web Engine & Ad-Blocking
- **Three-Tier Ads Watchdog** — Integrated background interceptor that instantly neutralizes audio ads, blocks network tracking hosts, and reactive-hides DOM banner elements via custom JS/CSS injections.
- **Bi-Directional JavaScript Bridge** — Zero-latency reactive communication channel between Chromium and native Kotlin to synchronize player states in real-time.
- **Flawless Background Playback** — Heavily tuned lifecycle management that prevents the Android system from killing the audio stream when minimized or locked.

### 🎤 Interactive Lyrics Engine (YT Music Style)
- **Multi-Strategy API Fetching** — Concurrent multi-thread network requests (`lrclib`) with smart full-text token scoring and automated Unicode (Japanese/Cyrillic) sanitization.
- **Click-to-Seek Navigation** — Instantly navigate through the song's timeline by tapping directly on any specific text line.
- **Smooth Auto-Scrolling** — Adaptive viewport tracking with built-in protection that pauses automatic centering whenever manual user scrolling is in progress.
- **Two-Layer Caching** — Lightning-fast in-memory `LruCache` paired with local JSON disk serialization and automatic legacy cache migration.

### ⚙️ Maintenance & System Control
- **MediaSession Core** — Complete native integration with the Android system notification drawer, lock screen controllers, and system media widgets.
- **Remote Update System** — GitHub/Netlify JSON-driven version manager supporting both soft update prompts and critical blocking overlays.

---

## 🏗️ Architecture & Tech Stack

The internal infrastructure of the project is built upon rigorous production-grade patterns, ensuring loose coupling and absolute separation of concerns:

- **Clean Architecture & UDF** — Complete separation into decoupled Data, UI (Presentation), and Web-Engine layers guided by Unidirectional Data Flow.
- **Asynchronous Flow** — Driven entirely by Kotlin Coroutines, StateFlow, and high-speed Channels for non-blocking concurrent operations.
- **Tech Stack Core** — Jetpack Compose, Modern WebView Engine, Custom Monet Integration, Coroutines, OkHttp, Gson.

---

## 📥 Download & Community

All production-ready stable `.apk` binaries are distributed exclusively via the community channel.

1. Go to the official [Telegram Channel](https://t.me/spot_app_player).
2. Download the latest compiled package from the pinned release messages.
3. Grant installation permissions for unknown sources in your Android settings and launch the app.

---

## 🔒 Legal Notice

This software is an independent browser wrapper built for educational purposes and personal interface optimization. It works strictly as a client-side layout customizer and does not bypass subscription barriers, modify server data, or breach web protocols.

- Spot is not affiliated with, maintained by, or endorsed by any official music streaming services.
- All product names, trademarks, and registered logos are property of their respective owners.