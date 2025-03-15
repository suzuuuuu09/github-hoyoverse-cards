import type { GameOption, GameCode, LangOption, LangCode } from '$lib/types';

export const GAME_MAP: Record<GameOption, GameCode> = {
  "Genshin Impact": "gi",
  "Honkai Star Rail": "hsr",
  "Zenless Zone Zero": "zzz"
};

export const LANG_MAP: Record<LangOption, LangCode> = {
  "简体中文": "zh-CN",
  "繁體中文": "zh-TW",
  "English": "en",
  "日本語": "ja",
  "한국어": "ko"
};

export const DEFAULT_VALUES = {
  GAME: "Genshin Impact" as GameOption,
  LANG: "English" as LangOption,
  HIDE_UID: false,
  TOP_ALIGN: "Left" as const,
  BOTTOM_ALIGN: "Right" as const,
  RADIUS: 10,
  BASE_URL: 'https://github-hoyoverse-cards.vercel.app',
} as const;