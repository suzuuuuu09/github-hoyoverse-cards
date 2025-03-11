<script lang="ts">
  import { Card, CodeBlock, ImagePreview } from "$lib/components";
  import { urlParams } from "$lib/stores/settings";
  import { DEFAULT_VALUES } from "$lib/constants/mappings";
  import type { GameCode, LangCode } from "$lib/types";

  export let game: GameCode;
  export let uid: string;
  export let bg: string;
  export let lang: LangCode;
  export let hideUid: boolean;
  export let top: string;
  export let bottom: string;

  $: markdownCode = `[![Github HoYoverse Card](${$urlParams.baseUrl}/api/card/${$urlParams.gameCode}/?uid=${$urlParams.uid}${$urlParams.queryString ? `&${$urlParams.queryString}` : ''})](${DEFAULT_VALUES.BASE_URL})`;
  $: htmlCode = `<a href='${DEFAULT_VALUES.BASE_URL}'><img src='${$urlParams.baseUrl}/api/card/${$urlParams.gameCode}/?uid=${$urlParams.uid}${$urlParams.queryString ? `&${$urlParams.queryString}` : ''}' alt='Github HoYoverse Card'></a>`;
</script>

<Card>
  <h2 class="text-3xl mb-3 font-bold text-center text-gray-900 dark:text-white duration-300">Preview</h2>
  {#if uid.trim()}
    <ImagePreview
      {game}
      {uid}
      {bg}
      {lang}
      {hideUid}
      {top}
      {bottom}
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