<script lang="ts">
  import { createEventDispatcher } from 'svelte';

  export let checked: boolean = false;
  export let label: string = '';
  export let disabled: boolean = false;

  const dispatch = createEventDispatcher();

  function handleChange() {
    if (!disabled) {
      dispatch('change', { checked: !checked });
    }
  }
</script>

<label class="relative inline-flex items-center cursor-pointer">
  <input
    type="checkbox"
    class="sr-only peer"
    {checked}
    {disabled}
    on:change={handleChange}
  />
  <div class="w-11 h-6 bg-gray-200 dark:bg-gray-700 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600 duration-300"></div>
  {#if label}
    <span class="ms-3 text-sm font-medium text-gray-900 dark:text-white">{label}</span>
  {/if}
</label>