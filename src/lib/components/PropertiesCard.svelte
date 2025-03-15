<script lang="ts">
  import { Card, Dropdown, InputField, Information, Toggle, Slider } from "$lib/components";
  import { settings } from "$lib/stores/settings";
  import { GAME_MAP, LANG_MAP } from "$lib/constants/mappings";
  import type { GameOption, LangOption } from "$lib/types";

  function handleGameSelect(event: CustomEvent<{ selectedOption: GameOption }>) {
    settings.update(s => ({ ...s, game: event.detail.selectedOption }));
  }

  function handleLangSelect(event: CustomEvent<{ selectedOption: LangOption }>) {
    settings.update(s => ({ ...s, lang: event.detail.selectedOption }));
  }

  function handleHideUidSelect(event: CustomEvent<{ selectedOption: string }>) {
    settings.update(s => ({ ...s, hideUid: event.detail.selectedOption === "True" }));
  }

  function handleTopSelect(event: CustomEvent<{ selectedOption: "Left" | "Center" | "Right" }>) {
    settings.update(s => ({ ...s, topAlign: event.detail.selectedOption }));
  }

  function handleBottomSelect(event: CustomEvent<{ selectedOption: "Left" | "Center" | "Right" }>) {
    settings.update(s => ({ ...s, bottomAlign: event.detail.selectedOption }));
  }

  function handleBorderToggle(event: CustomEvent<{ checked: boolean }>) {
    settings.update(s => ({ ...s, borderEnabled: event.detail.checked }));
  }

  function handleBorderWidthChange(event: CustomEvent<{ value: number }>) {
    settings.update(s => ({ ...s, borderWidth: event.detail.value }));
  }
</script>

<Card>
  <h2 class="text-3xl mb-3 font-bold text-center text-gray-900 dark:text-white duration-300">Properties</h2>
  
  <!-- Game Selection -->
  <div class="flex my-1.5 items-center justify-between">
    <div class="flex items-center gap-1">
      <label for="game" class="text-gray-900 dark:text-white after:text-red-500 after:content-['*']">Game</label>
      <Information>Select the HoYoverse game you want to display stats for</Information>
    </div>
    <Dropdown
      id="game"
      options={Object.keys(GAME_MAP)}
      initialSelectedOption={$settings.game}
      on:select={handleGameSelect}
    />
  </div>

  <!-- UID -->
  <div class="flex my-1.5 items-center justify-between">
    <div class="flex items-center gap-1">
      <label for="uid" class="text-gray-900 dark:text-white after:text-red-500 after:content-['*']">UID</label>
      <Information>Your in-game UID number</Information>
    </div>
    <InputField
      id="uid"
      type="text"
      placeholder="Type UID..."
      bind:value={$settings.uid}
    />
  </div>
  
  <!-- Background ID -->
  <div class="flex my-1.5 items-center justify-between">
    <div class="flex items-center gap-1">
      <label for="bg-id" class="text-gray-900 dark:text-white">Background</label>
      <Information>Custom background ID for your card</Information>
    </div>
    <InputField
      id="bg"
      type="text"
      placeholder="Type Background ID..."
      bind:value={$settings.bgId}
    />
  </div>

  <!-- Language -->
  <div class="flex my-1.5 items-center justify-between">
    <div class="flex items-center gap-1">
      <label for="lang" class="text-gray-900 dark:text-white">Language</label>
      <Information>Display language for the card content</Information>
    </div>
    <Dropdown
      id="lang"
      options={Object.keys(LANG_MAP)}
      initialSelectedOption={$settings.lang}
      on:select={handleLangSelect}
    />
  </div>

  <!-- Hide UID -->
  <div class="flex my-1.5 items-center justify-between">
    <div class="flex items-center gap-1">
      <label for="hide-uid" class="text-gray-900 dark:text-white">Hide UID</label>
      <Information>Option to hide your UID from the display</Information>
    </div>
    <Dropdown
      id="hide-uid"
      options={["True", "False"]}
      initialSelectedOption={$settings.hideUid ? "True" : "False"}
      on:select={handleHideUidSelect}
    />
  </div>
  
  <!-- Top Alignment -->
  <div class="flex my-1.5 items-center justify-between">
    <div class="flex items-center gap-1">
      <label for="top" class="text-gray-900 dark:text-white">Top</label>
      <Information>Alignment for the top section of the card</Information>
    </div>
    <Dropdown
      id="top"
      options={["Left", "Center", "Right"]}
      initialSelectedOption={$settings.topAlign}
      on:select={handleTopSelect}
    />
  </div>

  <!-- Bottom Alignment -->
  <div class="flex my-1.5 items-center justify-between">
    <div class="flex items-center gap-1">
      <label for="bottom" class="text-gray-900 dark:text-white">Bottom</label>
      <Information>Alignment for the bottom section of the card</Information>
    </div>
    <Dropdown
      id="bottom"
      options={["Left", "Center", "Right"]}
      initialSelectedOption={$settings.bottomAlign}
      on:select={handleBottomSelect}
    />
  </div>

  <!-- Rounded Corner -->
  <div class="flex my-1.5 items-center justify-between">
    <div class="flex items-center gap-1">
      <label for="radius" class="text-gray-900 dark:text-white">Rounded Corner</label>
      <Information>Corner roundness of the card (0-20)</Information>
    </div>
    <InputField
      id="radius"
      type="number"
      placeholder="Corner radius..."
      min={0}
      max={20}
      bind:value={$settings.radius}
    />
  </div>

  <details class="mt-3">
    <summary class="text-gray-900 dark:text-white cursor-pointer">Border Settings</summary>
    <div class="mt-3 space-y-4 ml-3">
      <!-- Border Enable/Disable -->
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-1">
          <label for="border-enabled" class="text-gray-900 dark:text-white">Enable Border</label>
          <Information>Toggle border visibility</Information>
        </div>
        <Toggle
          checked={$settings.borderEnabled}
          on:change={handleBorderToggle}
        />
      </div>

      <!-- Border Width -->
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-1">
          <label for="border-width" class="text-gray-900 dark:text-white">Border Width</label>
          <Information>Width of the border (1-10px)</Information>
        </div>
        <div class="w-1/2">
          <Slider
            min={1}
            max={10}
            value={$settings.borderWidth}
            active={$settings.borderEnabled}
            disabled={!$settings.borderEnabled}
            unit="px"
            on:change={handleBorderWidthChange}
          />
        </div>
      </div>

      <!-- Border Color -->
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-1">
          <label for="border-color" class="text-gray-900 dark:text-white">Border Color</label>
          <Information>Color of the border</Information>
        </div>
        <div class="flex items-center gap-2">
          <input
            type="color"
            id="border-color"
            bind:value={$settings.borderColor}
            class="w-12 h-8 p-0 border-0 cursor-pointer"
            class:opacity-50={!$settings.borderEnabled}
            disabled={!$settings.borderEnabled}
            on:input={(e) => {
              const target = e.target as HTMLInputElement;
              settings.update(s => ({ ...s, borderColor: target.value }));
            }}
          />
          <input
            type="text"
            value={$settings.borderColor.toUpperCase()}
            class="w-20 px-2 py-1 text-sm border border-gray-300 rounded dark:bg-gray-800 dark:border-gray-700 dark:text-gray-100"
            class:opacity-50={!$settings.borderEnabled}
            placeholder="#FFFFFF"
            disabled={!$settings.borderEnabled}
            on:input={(e) => {
              const target = e.target as HTMLInputElement;
              let value = target.value;
              
              // #を自動的に追加
              if (!value.startsWith('#')) {
                value = '#' + value;
              }
              
              // 有効な16進数カラーコードの場合のみ更新
              if (/^#[0-9A-Fa-f]{6}$/.test(value)) {
                settings.update(s => ({ ...s, borderColor: value }));
              }
            }}
          />
        </div>
      </div>
    </div>
  </details>
</Card>