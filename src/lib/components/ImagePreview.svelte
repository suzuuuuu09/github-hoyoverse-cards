<script lang="ts">
  export let game: 'gi' | 'hsr' | 'zzz' = 'gi';
  export let uid: string = '';
  export let bg: string = '';
  export let lang: string = 'en';
  export let hideUid: boolean = false;
  export let top: string = '';
  export let bottom: string = '';

  $: baseUrl = typeof window !== 'undefined' ? window.location.origin : 'https://hv-cards.vercel.app';
  $: imageUrl = `${baseUrl}/api/card/${game}/?uid=${uid}${bg ? `&bg=${bg}` : ''}${lang !== 'en' ? `&lang=${lang}` : ''}${hideUid ? '&hide_uid=true' : ''}${top ? `&top=${top}` : ''}${bottom ? `&bottom=${bottom}` : ''}`;
</script>

<div class="w-full max-w-[800px] mx-auto my-4 rounded-lg overflow-hidden">
  {#if uid.trim()}
    <img
      src={imageUrl}
      alt="Profile Card Preview"
      class="w-full h-auto block"
    />
  {:else}
    <div class="p-8 text-center bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white rounded-lg">
      Please enter a UID to preview the card
    </div>
  {/if}
</div>