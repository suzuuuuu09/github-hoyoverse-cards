# hv-cards

Hoyoverseゲームのプロフィールカード

## 説明

Hoyoverseのゲーム、「原神」や「崩壊スターレイル」、「ゼンレスゾーンゼロ」などのプロフィールカードを作成する。<br>
Githubでの使用を目的としている。

## 使い方

| パラメータ | 説明 | 必須 | 初期値 |
| :---: | :---: | :---: | :---: |
| `game` | ゲームの種類 | o | gi |
| `uid` | ゲーム内のUID | o | 800000000 |
| `bg` | 背景画像 | x | 1 |
| `bg_color` | 背景色 | x |  |
| `locale` | 言語 | x | en |
| `hide_uid` |  |  | false |

```text
https://hv-cards.vercel.app/api/{game}/?uid={uid}
```

### ゲームID

| ゲームID | ゲーム名 |
| :---: | :---: |
| `gi` | 原神 |
| `hsr` | 崩壊スターレイル |
| `zzz` | ゼンレスゾーンゼロ |
