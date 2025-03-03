<script lang="ts">
  import Icon from "@iconify/svelte";
  import { Card, ThemeToggle, CodeBlock, Dropdown, ImagePreview, InputField, Information } from "$lib/components";
  import { settings, urlParams } from "$lib/stores/settings";
  import { GAME_MAP, LANG_MAP, DEFAULT_VALUES } from "$lib/constants/mappings";
  import type { GameOption, LangOption } from "$lib/types";

  $: markdownCode = `[![Github HoYoverse Card](${$urlParams.baseUrl}/api/card/${$urlParams.gameCode}/?uid=${$urlParams.uid}${$urlParams.queryString ? `&${$urlParams.queryString}` : ''})](${DEFAULT_VALUES.BASE_URL})`;
  $: htmlCode = `<a href='${DEFAULT_VALUES.BASE_URL}'><img src='${$urlParams.baseUrl}/api/card/${$urlParams.gameCode}/?uid=${$urlParams.uid}${$urlParams.queryString ? `&${$urlParams.queryString}` : ''}' alt='Github HoYoverse Card'></a>`;

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

<main class="min-h-screen p-8 bg-gray-100 dark:bg-gray-900 duration-300">
  <h1 class="text-4xl text-center font-bold text-gray-900 dark:text-white duration-300">GitHub HoYoverse Cards</h1>
  <div class="max-w-6xl mx-auto">
    <div class="flex justify-end mb-8">
      <ThemeToggle />
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <!-- PropertiesCard -->
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

      <!-- PreviewCard -->
      <Card>
        <h2 class="text-3xl mb-3 font-bold text-center text-gray-900 dark:text-white duration-300">Preview</h2>
        {#if $settings.uid.trim()}
          <ImagePreview
            game={$urlParams.gameCode}
            uid={$settings.uid}
            bg={$settings.bgId}
            lang={LANG_MAP[$settings.lang]}
            hideUid={$settings.hideUid}
            top={$settings.topAlign.toLowerCase()}
            bottom={$settings.bottomAlign.toLowerCase()}
          />
        {:else}
          <div class="flex flex-wrap w-full max-w-[800px] px-4 py-15 text-center justify-center bg-gray-100 dark:bg-slate-900 text-gray-900 dark:text-white rounded-lg duration-300">
            <p class="text-center text-gray-900 dark:text-white duration-300">Please enter a UID to see the preview.</p>
          </div>
        {/if}

        <!-- Markdown Preview -->
        <h3 class="text-xl my-3 font-bold text-gray-900 dark:text-white duration-300">Markdown</h3>
        <CodeBlock code={markdownCode}/>

        <!-- HTML Preview -->
        <h3 class="text-xl my-3 font-bold text-gray-900 dark:text-white duration-300">HTML</h3>
        <CodeBlock code={htmlCode}/>
      </Card>
    </div>
  </div>

  <footer class="flex justify-center mt-8">
    <button
      class="p-2 rounded-lg hover:bg-slate-300 dark:hover:bg-slate-700 duration-300 relative"
      on:click={() => location.href='https://github.com/suzuuuuu09/github-hv-cards'}
      title="View on GitHub"
      style="cursor:pointer"
    >
      <Icon icon="mdi:github" class="w-8 h-8 text-gray-900 dark:text-white duration-300" />
    </button>
  </footer>
</main>