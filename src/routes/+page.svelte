<script lang="ts">
  import Icon from "@iconify/svelte";
  import { Card, ThemeToggle, CodeBlock, Dropdown, ImagePreview, InputField, Information } from "$lib/components";
  
  const gameMap = {
    "Genshin Impact": "gi",
    "Honkai Star Rail": "hsr",
    "Zenless Zone Zero": "zzz"
  } as const;

  const langMap = {
    "简体中文": "cn",
    "繁體中文": "tw",
    "English": "en",
    "日本語": "jp",
    "한국어": "kr"
  } as const;

  type GameOption = keyof typeof gameMap;
  type LangOption = keyof typeof langMap;

  let selectedGameOption: GameOption = "Genshin Impact";
  let selectedLangOption: LangOption = "English";
  let selectedHideUidOption = false;
  let selectedTopOption = "Left";
  let selectedBottomOption = "Right";
  let uid = "";
  let bgId = "";

  $: gameParam = gameMap[selectedGameOption];
  $: langParam = langMap[selectedLangOption];
  $: baseUrl = typeof window !== 'undefined' ? window.location.origin : 'https://github-hv-cards.vercel.app';
  $: markdownCode = `[![Github HoYoverse Card](${baseUrl}/api/card/${gameParam}/?uid=${uid}${bgId ? `&bg=${bgId}` : ''}${langParam !== 'en' ? `&lang=${langParam}` : ''}${selectedHideUidOption ? '&hide_uid=true' : ''}${selectedTopOption.toLowerCase() !== 'left' ? `&top=${selectedTopOption.toLowerCase()}` : ''}${selectedBottomOption.toLowerCase() !== 'right' ? `&bottom=${selectedBottomOption.toLowerCase()}` : ''})](https://github-hv-cards.vercel.app/)`;
  $: htmlCode = `<a href='https://github-hv-cards.vercel.app/'><img src='${baseUrl}/api/card/${gameParam}/?uid=${uid}${bgId ? `&bg=${bgId}` : ''}${langParam !== 'en' ? `&lang=${langParam}` : ''}${selectedHideUidOption ? '&hide_uid=true' : ''}${selectedTopOption.toLowerCase() !== 'left' ? `&top=${selectedTopOption.toLowerCase()}` : ''}${selectedBottomOption.toLowerCase() !== 'right' ? `&bottom=${selectedBottomOption.toLowerCase()}` : ''}' alt='Github HoYoverse Card'></a>`;

  function handleGameSelect(event: CustomEvent<{ selectedOption: GameOption }>) {
    selectedGameOption = event.detail.selectedOption;
  }

  function handleLangSelect(event: CustomEvent<{ selectedOption: LangOption }>) {
    selectedLangOption = event.detail.selectedOption;
  }

  function handleHideUidSelect(event: CustomEvent<{ selectedOption: boolean }>) {
    selectedHideUidOption = event.detail.selectedOption;
  }

  function handleTopSelect(event: CustomEvent<{ selectedOption: string }>) {
    selectedTopOption = event.detail.selectedOption;
  }

  function handleBottomSelect(event: CustomEvent<{ selectedOption: string }>) {
    selectedBottomOption = event.detail.selectedOption;
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
        
        <!-- 項目1(ゲーム選択) -->
        <div class="flex my-1.5 items-center justify-between">
          <div class="flex items-center gap-1">
            <label for="game" class="text-gray-900 dark:text-white">Game<span class="text-red-500">*</span></label>
            <Information>Select the HoYoverse game you want to display stats for</Information>
          </div>
          <Dropdown
            id="game"
            options={["Genshin Impact", "Honkai Star Rail", "Zenless Zone Zero"]}
            initialSelectedOption={selectedGameOption}
            on:select={handleGameSelect}
          />
        </div>

        <!-- 項目2(UID) -->
        <div class="flex my-1.5 items-center justify-between">
          <div class="flex items-center gap-1">
            <label for="uid" class="text-gray-900 dark:text-white">UID<span class="text-red-500">*</span></label>
            <Information>Your in-game UID number</Information>
          </div>
          <InputField
            id="uid"
            type="text"
            placeholder="Type UID..."
            bind:value={uid}
          />
        </div>
        
        <!-- 項目3(背景ID) -->
        <div class="flex my-1.5 items-center justify-between">
          <div class="flex items-center gap-1">
            <label for="bg-id" class="text-gray-900 dark:text-white">Background</label>
            <Information>Custom background ID for your card</Information>
          </div>
          <InputField
            id="bg"
            type="text"
            placeholder="Type Background ID..."
            bind:value={bgId}
          />
        </div>

        <!-- 項目4(言語選択) -->
        <div class="flex my-1.5 items-center justify-between">
          <div class="flex items-center gap-1">
            <label for="lang" class="text-gray-900 dark:text-white">Language</label>
            <Information>Display language for the card content</Information>
          </div>
          <Dropdown
            id="lang"
            options={["简体中文", "繁體中文", "English", "日本語", "한국어"]}
            initialSelectedOption={selectedLangOption}
            on:select={handleLangSelect}
          />
        </div>

        <!-- 項目5(UID隠す) -->
        <div class="flex my-1.5 items-center justify-between">
          <div class="flex items-center gap-1">
            <label for="hide-uid" class="text-gray-900 dark:text-white">Hide UID</label>
            <Information>Option to hide your UID from the display</Information>
          </div>
          <Dropdown
            id="hide-uid"
            options={["True", "False"]}
            initialSelectedOption={selectedHideUidOption ? "True" : "False"}
            on:select={(event) => handleHideUidSelect(new CustomEvent('select', { detail: { selectedOption: event.detail.selectedOption === "True" } }))}
          />
        </div>
        
        <!-- 項目6(TOP) -->
        <div class="flex my-1.5 items-center justify-between">
          <div class="flex items-center gap-1">
            <label for="top" class="text-gray-900 dark:text-white">Top</label>
            <Information>Alignment for the top section of the card</Information>
          </div>
          <Dropdown
            id="top"
            options={["Left", "Center", "Right"]}
            initialSelectedOption={selectedTopOption}
            on:select={handleTopSelect}
          />
        </div>

        <!-- 項目7(BOTTOM) -->
        <div class="flex my-1.5 items-center justify-between">
          <div class="flex items-center gap-1">
            <label for="bottom" class="text-gray-900 dark:text-white">Bottom</label>
            <Information>Alignment for the bottom section of the card</Information>
          </div>
          <Dropdown
            id="bottom"
            options={["Left", "Center", "Right"]}
            initialSelectedOption={selectedBottomOption}
            on:select={handleBottomSelect}
          />
        </div>
      </Card>
      <!-- PreviewCard -->
      <Card>
        <h2 class="text-3xl mb-3 font-bold text-center text-gray-900 dark:text-white duration-300">Preview</h2>
        {#if uid.trim()}
          <ImagePreview
            game={gameParam}
            uid={uid}
            bg={bgId}
            lang={langParam}
            hideUid={selectedHideUidOption}
            top={selectedTopOption.toLowerCase()}
            bottom={selectedBottomOption.toLowerCase()}
          />
        {:else}
        <div class="flex flex-wrap w-full max-w-[800px] px-4 py-15 text-center justify-center bg-gray-100 dark:bg-slate-900 text-gray-900 dark:text-white rounded-lg duration-300">
          <p class="text-center text-gray-900 dark:text-white duration-300">Please enter a UID to see the preview.</p>
        </div>
        {/if}
        <!-- MarkdownPreview -->
        <h3 class="text-xl my-3 font-bold text-gray-900 dark:text-white duration-300">Markdown</h3>
        <CodeBlock code={markdownCode}/>
        <!-- HTMLPreview -->
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