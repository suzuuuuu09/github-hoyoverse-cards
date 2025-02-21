<script lang="ts">
  import { createEventDispatcher } from 'svelte';

  export let options: string[] = [];
  export let initialSelectedOption: string = "Menu";

  let isOpen = false;
  let selectedOption = initialSelectedOption;

  const dispatch = createEventDispatcher();

  function toggleDropdown() {
    isOpen = !isOpen;
  }

  function selectOption(option: string) {
    selectedOption = option;
    isOpen = false; // ドロップダウンを閉じる
    dispatch('select', { selectedOption: option });
  }
</script>

<button
  on:click={toggleDropdown}
  class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none"
>
  {selectedOption}
</button>
{#if isOpen}
  <div class="absolute mt-2 w-48 rounded-md shadow-lg bg-white dark:bg-gray-800 ring-1 ring-black ring-opacity-5 max-h-60 overflow-y-auto">
    <div class="py-1" role="menu">
      {#each options as option}
        <button
          class="block w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700"
          on:click={() => selectOption(option)}
        >
          {option}
        </button>
      {/each}
    </div>
  </div>
{/if}