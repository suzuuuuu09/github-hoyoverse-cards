<script lang="ts">
  import { Card, Dropdown, InputField, Information } from "$lib/components";
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
</script>

<Card>
  <h2 class="text-3xl mb-3 font-bold text-center text-gray-900 dark:text-white duration-300">Properties</h2>
  
  <!-- Game Selection -->
  <div class="flex my-1.5 items-center justify-between">
    <div class="flex items-center gap-1">
      <label for="game" class="text-gray-900 dark:text-white">Game<span class="text-red-500">*</span></label>
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
      <label for="uid" class="text-gray-900 dark:text-white">UID<span class="text-red-500">*</span></label>
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
</Card>