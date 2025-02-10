# hv-cards

HoYoverseゲームのプロフィールカード

## 説明

HoYoverseのゲーム、「原神」や「崩壊スターレイル」、「ゼンレスゾーンゼロ」のプロフィールカードを作成する。<br>
Githubでの使用を目的としている。

## 使い方

| パラメータ | 説明 | 必須 | 初期値 |
| :---: | :---: | :---: | :---: |
| `game` | ゲームの種類 | o | gi |
| `uid` | ゲーム内のUID | o |  |
| `bg` | 背景画像 | x |  |
| `bg_color` | 背景色 | x |  |
| `lang` | 言語 | x | en |
| `hide_uid` |  |  | false |
| `top` |  |  |  |
| `bottom` |  |  |  |

```text
https://hv-cards.vercel.app/api/{game}/?uid={uid}
```

### ゲームID

| ゲームID | ゲーム名 |
| :---: | :---: |
| `gi` | 原神 |
| `hsr` | 崩壊スターレイル |
| `zzz` | ゼンレスゾーンゼロ |
