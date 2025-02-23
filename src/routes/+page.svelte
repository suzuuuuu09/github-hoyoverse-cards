<script lang="ts">
  import ThemeToggle from "$lib/components/buttons/ThemeToggleButton.svelte";
  import Card from "$lib/components/Card.svelte";
  import Dropdown from "$lib/components/Dropdown.svelte";
  import InputField from "$lib/components/InputField.svelte";
  import CodeBlock from "$lib/components/CodeBlock.svelte";
  import ImagePreview from "$lib/components/ImagePreview.svelte";
  
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
  $: baseUrl = typeof window !== 'undefined' ? window.location.origin : 'https://hv-cards.vercel.app';
  $: markdownCode = `[![Github HoYoverse Card](${baseUrl}/api/card/${gameParam}/?uid=${uid}${bgId ? `&bg=${bgId}` : ''}${langParam !== 'en' ? `&lang=${langParam}` : ''}${selectedHideUidOption ? '&hide_uid=true' : ''}${selectedTopOption.toLowerCase() !== 'left' ? `&top=${selectedTopOption.toLowerCase()}` : ''}${selectedBottomOption.toLowerCase() !== 'right' ? `&bottom=${selectedBottomOption.toLowerCase()}` : ''})](https://hv-cards.vercel.app/)`;
  $: htmlCode = `<a href='https://hv-cards.vercel.app/'><img src='${baseUrl}/api/card/${gameParam}/?uid=${uid}${bgId ? `&bg=${bgId}` : ''}${langParam !== 'en' ? `&lang=${langParam}` : ''}${selectedHideUidOption ? '&hide_uid=true' : ''}${selectedTopOption.toLowerCase() !== 'left' ? `&top=${selectedTopOption.toLowerCase()}` : ''}${selectedBottomOption.toLowerCase() !== 'right' ? `&bottom=${selectedBottomOption.toLowerCase()}` : ''}' alt='Github HoYoverse Card'></a>`;

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
          <label for="game" class="text-gray-900 dark:text-white">Game<span class="text-red-500">*</span></label>
          <Dropdown
            id="game"
            options={["Genshin Impact", "Honkai Star Rail", "Zenless Zone Zero"]}
            initialSelectedOption={selectedGameOption}
            on:select={handleGameSelect}
          />
        </div>

        <!-- 項目2(UID) -->
        <div class="flex my-1.5 items-center justify-between">
          <label for="uid" class="text-gray-900 dark:text-white">UID<span class="text-red-500">*</span></label>
          <InputField
            id="uid"
            type="text"
            placeholder="Type UID..."
            bind:value={uid}
          />
        </div>
        
        <!-- 項目3(背景ID) -->
        <div class="flex my-1.5 items-center justify-between">
          <label for="bg-id" class="text-gray-900 dark:text-white">Background</label>
          <InputField
            id="bg"
            type="text"
            placeholder="Type Background ID..."
            bind:value={bgId}
          />
        </div>

        <!-- 項目4(言語選択) -->
        <div class="flex my-1.5 items-center justify-between">
          <label for="lang" class="text-gray-900 dark:text-white">Language</label>
          <Dropdown
            id="lang"
            options={["简体中文", "繁體中文", "English", "日本語", "한국어"]}
            initialSelectedOption={selectedLangOption}
            on:select={handleLangSelect}
          />
        </div>

        <!-- 項目5(UID隠す) -->
        <div class="flex my-1.5 items-center justify-between">
          <label for="hide-uid" class="text-gray-900 dark:text-white">Hide UID</label>
          <Dropdown
            id="hide-uid"
            options={["True", "False"]}
            initialSelectedOption={selectedHideUidOption ? "True" : "False"}
            on:select={(event) => handleHideUidSelect(new CustomEvent('select', { detail: { selectedOption: event.detail.selectedOption === "True" } }))}
          />
        </div>
        
        <!-- 項目6(TOP) -->
        <div class="flex my-1.5 items-center justify-between">
          <label for="top" class="text-gray-900 dark:text-white">Top</label>
          <Dropdown
            id="top"
            options={["Left", "Center", "Right"]}
            initialSelectedOption={selectedTopOption}
            on:select={handleTopSelect}
          />
        </div>

        <!-- 項目7(BOTTOM) -->
        <div class="flex my-1.5 items-center justify-between">
          <label for="bottom" class="text-gray-900 dark:text-white">Bottom</label>
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
</main>