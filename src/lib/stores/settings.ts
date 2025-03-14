import { writable, derived } from 'svelte/store';
import type { GameOption, LangOption } from '$lib/types';
import { GAME_MAP, LANG_MAP, DEFAULT_VALUES } from '$lib/constants/mappings';

interface Settings {
  game: GameOption;
  uid: string;
  bgId: string;
  lang: LangOption;
  hideUid: boolean;
  topAlign: 'Left' | 'Center' | 'Right';
  bottomAlign: 'Left' | 'Center' | 'Right';
  radius: number;
  borderEnabled: boolean;
  borderWidth: number;
  borderColor: string;
}

export const settings = writable<Settings>({
  game: DEFAULT_VALUES.GAME,
  uid: '',
  bgId: '',
  lang: DEFAULT_VALUES.LANG,
  hideUid: DEFAULT_VALUES.HIDE_UID,
  topAlign: DEFAULT_VALUES.TOP_ALIGN,
  bottomAlign: DEFAULT_VALUES.BOTTOM_ALIGN,
  radius: DEFAULT_VALUES.RADIUS,
  borderEnabled: false,
  borderWidth: 2,
  borderColor: '#ffffff'
});

export const baseUrl = writable(DEFAULT_VALUES.BASE_URL);

export const urlParams = derived(
  [settings, baseUrl],
  ([$settings, $baseUrl]) => {
    const params = new URLSearchParams();
    const gameCode = GAME_MAP[$settings.game];
    const langCode = LANG_MAP[$settings.lang];

    if ($settings.bgId) params.set('bg', $settings.bgId);
    if (langCode !== 'en') params.set('lang', langCode);
    if ($settings.hideUid) params.set('hide_uid', 'true');
    if ($settings.topAlign.toLowerCase() !== 'left') params.set('top', $settings.topAlign.toLowerCase());
    if ($settings.bottomAlign.toLowerCase() !== 'right') params.set('bottom', $settings.bottomAlign.toLowerCase());
    if ($settings.radius !== DEFAULT_VALUES.RADIUS) params.set('radius', $settings.radius.toString());
    if ($settings.borderEnabled) {
      params.set('border_width', $settings.borderWidth.toString());
      params.set('border_color', $settings.borderColor.replace('#', ''));
    }

    return {
      gameCode,
      baseUrl: $baseUrl,
      uid: $settings.uid,
      queryString: params.toString()
    };
  }
);