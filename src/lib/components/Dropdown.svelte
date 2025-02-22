<script lang="ts">
  import Icon from '@iconify/svelte'
  import { createEventDispatcher, onMount } from 'svelte';
  import { activeDropdownId } from '$lib/stores/dropdown';

  export let options: string[] = [];
  export let initialSelectedOption: string = "Menu";
  export let id: string;

  let isOpen = false;
  let selectedOption = initialSelectedOption;
  let dropdownContainer: HTMLElement;

  const dispatch = createEventDispatcher();

  activeDropdownId.subscribe(activeId => {
    if (activeId !== id) {
      isOpen = false;
    }
  });

  onMount(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownContainer && !dropdownContainer.contains(event.target as Node)) {
        isOpen = false;
        activeDropdownId.set(null);
      }
    };

    document.addEventListener('click', handleClickOutside);

    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  });

  function toggleDropdown(event: MouseEvent) {
    event.stopPropagation();
    isOpen = !isOpen;
    activeDropdownId.set(isOpen ? id : null);
  }

  function selectOption(option: string) {
    selectedOption = option;
    isOpen = false;
    activeDropdownId.set(null);
    dispatch('select', { selectedOption: option });
  }
</script>

<div class="relative w-1/2" bind:this={dropdownContainer}>
  <button
    on:click={toggleDropdown}
    class="w-full bg-blue-500 text-white flex items-center justify-between px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none"
  >
    {selectedOption}
    <Icon icon="gridicons:dropdown" class="w-5 h-5 inline-block" />
  </button>
  {#if isOpen}
    <div class="absolute w-full z-10 mt-2 rounded-md shadow-xl bg-white dark:bg-gray-800 ring-1 ring-black ring-opacity-5 max-h-60 overflow-y-auto">
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
</div>