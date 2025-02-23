<script lang="ts">
  import ThemeToggle from "$lib/components/buttons/ThemeToggleButton.svelte";
  import Card from "$lib/components/Card.svelte";
  import Dropdown from "$lib/components/Dropdown.svelte";
  import InputField from "$lib/components/InputField.svelte";
  import CodeBlock from "$lib/components/CodeBlock.svelte";
  
  let selectedLangOption = "English";
  let selectedGameOption = "Genshin Impact";
  let selectedHideUidOption = false;
  let selectedTopOption = "Left";
  let selectedBottomOption = "Right";

  function handleGameSelect(event: CustomEvent<{ selectedOption: string }>) {
    selectedGameOption = event.detail.selectedOption;
  }

  function handleLangSelect(event: CustomEvent<{ selectedOption: string }>) {
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

  const sampleCode = `
    function hello() {
      console.log("Hello, World!");
    }

    hello();
  `;
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
          />
        </div>
        
        <!-- 項目3(背景ID) -->
        <div class="flex my-1.5 items-center justify-between">
          <label for="bg-id" class="text-gray-900 dark:text-white">Background</label>
          <InputField
            id="bg"
            type="text"
            placeholder="Type Background ID..."
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
        
        <div class="pt-80 my-1.5 flex justify-center">
          <button
            class="w-1/6 bg-blue-500 text-white flex items-center justify-center px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none"
          >
            Generate
          </button>
        </div>
      </Card>

      <!-- PreviewCard -->
      <Card>
        <h2 class="text-3xl mb-3 font-bold text-center text-gray-900 dark:text-white duration-300">Preview</h2>
        <!-- MarkdownPreview -->
        <h3 class="text-xl my-3 font-bold text-gray-900 dark:text-white duration-300">Markdown</h3>
        <CodeBlock code="[![Github HoYoverse Card](https://hv-cards.vercel.app/api/card?uid=819312869)](https://hv-cards.vercel.app)"/>
        <!-- HTMLPreview -->
        <h3 class="text-xl my-3 font-bold text-gray-900 dark:text-white duration-300">HTML</h3>
        <CodeBlock code="<a href='https://hv-cards.vercel.app'><img src='https://hv-cards.vercel.app/api/card?uid=819312869' alt='Github HoYoverse Card'></a>"/>
      </Card>
    </div>
  </div>
</main>