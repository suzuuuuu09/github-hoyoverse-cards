<script lang="ts">
  import Icon from "$lib/components/Icon.svelte";
  import { mdiLoading } from "@mdi/js";
  import type { GameCode, LangCode } from "$lib/types";
  
  export let game: GameCode;
  export let uid: string = '';
  export let bg: string = '';
  export let lang: LangCode = 'en';
  export let hideUid: boolean = false;
  export let top: string = '';
  export let bottom: string = '';
  export let radius: number = 10;

  let isLoading = true;

  $: baseUrl = typeof window !== 'undefined' ? window.location.origin : 'https://github-hv-cards.vercel.app';
  $: imageUrl = `${baseUrl}/api/card/${game}/?uid=${uid}${bg ? `&bg=${bg}` : ''}${lang !== 'en' ? `&lang=${lang}` : ''}${hideUid ? '&hide_uid=true' : ''}${top ? `&top=${top}` : ''}${bottom ? `&bottom=${bottom}` : ''}${radius !== 10 ? `&radius=${radius}` : ''}`;

  function handleImageLoad() {
    isLoading = false;
  }
</script>

<div class="w-full max-w-[800px] mx-auto my-4 rounded-lg overflow-hidden relative">
  {#if uid.trim()}
    {#if isLoading}
      <div class="absolute inset-0 flex items-center justify-center bg-gray-100 dark:bg-gray-800">
        <Icon path={mdiLoading} class="w-12 h-12 text-gray-900 dark:text-white animate-spin" />
      </div>
    {/if}
    <img
      src={imageUrl}
      alt="Profile Card Preview"
      class="w-full h-auto block"
      on:load={handleImageLoad}
    />
  {:else}
    <div class="p-8 text-center bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white rounded-lg">
      Please enter a UID to preview the card
    </div>
  {/if}
</div>