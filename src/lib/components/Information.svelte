<script lang="ts">
  import Icon from "$lib/components/Icon.svelte";
  import { mdiHelpCircle } from "@mdi/js";
</script>

<div class="relative group">
  <Icon path={mdiHelpCircle} class="w-4 h-4 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200" />
  <div class="absolute z-50 left-1/2 -translate-x-1/2 bottom-full mb-2 px-3 py-2 w-48 bg-gray-900 dark:bg-gray-100 text-white dark:text-gray-900 text-sm rounded-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all">
    <slot />
  </div>
</div>