import type { GameOption, GameCode, LangOption, LangCode } from '$lib/types';

export const GAME_MAP: Record<GameOption, GameCode> = {
  "Genshin Impact": "gi",
  "Honkai Star Rail": "hsr",
  "Zenless Zone Zero": "zzz"
};

export const LANG_MAP: Record<LangOption, LangCode> = {
  "简体中文": "cn",
  "繁體中文": "tw",
  "English": "en",
  "日本語": "jp",
  "한국어": "kr"
};

export const DEFAULT_VALUES = {
  GAME: "Genshin Impact" as GameOption,
  LANG: "English" as LangOption,
  HIDE_UID: false,
  TOP_ALIGN: "Left" as const,
  BOTTOM_ALIGN: "Right" as const,
  BASE_URL: 'https://github-hv-cards.vercel.app'
} as const;