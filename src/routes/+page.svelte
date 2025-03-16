<script lang="ts">
  import Icon from "$lib/components/Icon.svelte";
  import { mdiGithub } from "@mdi/js";
  import { ThemeToggle } from "$lib/components";
  import PropertiesCard from "$lib/components/PropertiesCard.svelte";
  import PreviewCard from "$lib/components/PreviewCard.svelte";
  import { settings, urlParams } from "$lib/stores/settings";
  import { LANG_MAP } from "$lib/constants/mappings";
</script>

<main class="min-h-screen p-8 bg-gray-100 dark:bg-gray-900 duration-300">
  <h1 class="text-4xl text-center font-bold text-gray-900 dark:text-white duration-300">GitHub HoYoverse Cards</h1>
  <div class="max-w-6xl mx-auto">
    <div class="flex justify-end mb-8">
      <ThemeToggle />
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <PropertiesCard />
      <PreviewCard
        game={$urlParams.gameCode}
        uid={$settings.uid}
        bg={$settings.bgId}
        lang={LANG_MAP[$settings.lang]}
        hideUid={$settings.hideUid}
        top={$settings.topAlign.toLowerCase()}
        bottom={$settings.bottomAlign.toLowerCase()}
        radius={$settings.radius}
        borderWidth={$settings.borderEnabled ? $settings.borderWidth : 0}
        borderColor={$settings.borderColor}
        shadow={$settings.shadow}
      />
    </div>
  </div>

  <footer class="flex justify-center mt-8">
    <button
      class="cursor-pointer p-2 rounded-lg hover:bg-slate-300 dark:hover:bg-slate-700 duration-300 relative"
      on:click={() => location.href='https://github.com/suzuuuuu09/github-hoyoverse-cards'}
      title="View on GitHub"
    >
      <Icon path={mdiGithub} class="w-8 h-8 text-gray-900 dark:text-white duration-300" />
    </button>
  </footer>
 </main>
