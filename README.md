# 🎮 GitHub HoYoverse Cards

## 📝 概要

GitHub HoYoverse CardsはHoYoverse(miHoYo)が開発するゲームのプロフィールカードを生成するWebサービスです。
生成したカードはGitHubのプロフィールなどでの使用を想定しています。

## 🎯 対応状況

### ✅ 対応済みゲーム
- [原神 (Genshin Impact)](https://genshin.hoyoverse.com)

### 🚧 対応予定ゲーム
- [崩壊スターレイル (Honkai: Star Rail)](https://hsr.hoyoverse.com)
- [ゼンレスゾーンゼロ (Zenless Zone Zero)](https://zenless.hoyoverse.com)

## 💻 使い方

### 🔧 基本的な使用方法
```text
https://github-hv-cards.vercel.app/api/card/{game}/?uid={uid}
```

### ⚙️ パラメータ設定

| パラメータ | 説明 | 必須 | 初期値 | 選択可能な値 |
| :---: | :--- | :---: | :---: | :--- |
| `game` | ゲームの種類 | ✅ | gi | [ゲームID参照](#-ゲームid) |
| `uid` | ゲーム内のUID | ✅ | - | 数値 (例: `800000000`) |
| `bg` | 背景画像 | ❌ | - | [背景ID](assets/img/README.md)とは |
| `lang` | 表示言語 | ❌ | en | [言語コード参照](#-対応言語) |
| `hide_uid` | UIDの表示/非表示 | ❌ | false | `true` / `false` |
| `top` | 上部情報の位置 | ❌ | center | `left` / `center` / `right` |
| `bottom` | 下部情報の位置 | ❌ | center | `left` / `center` / `right` |
| `border_width` | 枠線の太さ | ❌ | 0 | `0` 〜 `10` |
| `border_color` | 枠線の色 | ❌ | ffffff | HEXカラーコード (例: `ff0000`) |

## 🎮 ゲームID

| ゲームID | ゲーム名 |
| :---: | :---: |
| `gi` | 原神 |
| `hsr` | 崩壊スターレイル |
| `zzz` | ゼンレスゾーンゼロ |

## 🌏 対応言語

| 言語ID | 言語 |
| :---: | :---: |
| en | English |
| zh-CN | 简体中文 |
| zh-TW | 繁體中文 |
| ja | 日本語 |
| ko | 한국어 |

### 📝 使用例
```markdown
基本的な使用方法:
![Genshin Impact Card](https://github-hv-cards.vercel.app/api/card/gi/?uid=800000000)

カスタマイズ例:
![Genshin Impact Card](https://github-hv-cards.vercel.app/api/card/gi/?uid=800000000&lang=jp&top=left&border_width=2&border_color=ff0000)
```

## 👥 貢献
プロジェクトへの貢献は大歓迎です！以下の方法で貢献できます：
- バグの報告
- 新機能の提案
- プルリクエストの送信
