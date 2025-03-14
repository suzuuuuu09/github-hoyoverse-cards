<script lang="ts">
  import { createEventDispatcher } from 'svelte';

  export let value: number;
  export let min: number = 0;
  export let max: number = 100;
  export let step: number = 1;
  export let active: boolean = true;
  export let disabled: boolean = false;
  export let showValue: boolean = true;
  export let unit: string = '';

  const dispatch = createEventDispatcher();

  function handleInput(event: Event) {
    const target = event.target as HTMLInputElement;
    const newValue = Number(target.value);
    dispatch('change', { value: newValue });
  }

  function handleNumberInput(event: Event) {
    const target = event.target as HTMLInputElement;
    let newValue = Number(target.value);
    
    // 範囲内に収める
    if (!isNaN(newValue)) {
      newValue = Math.max(min, Math.min(max, newValue));
      dispatch('change', { value: newValue });
    }
  }
</script>

<div class="flex items-center gap-2 w-full">
  <input
    type="range"
    {min}
    {max}
    {step}
    bind:value
    {disabled}
    on:input={handleInput}
    class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700
      [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-4 [&::-webkit-slider-thumb]:h-4 [&::-webkit-slider-thumb]:rounded-full 
      [&::-webkit-slider-thumb]:transition-colors
      [&::-webkit-slider-thumb]:border-0
      {active
        ? '[&::-webkit-slider-thumb]:bg-blue-500 hover:[&::-webkit-slider-thumb]:bg-blue-600'
        : '[&::-webkit-slider-thumb]:bg-gray-400 hover:[&::-webkit-slider-thumb]:bg-gray-500'
      }
      [&::-moz-range-thumb]:appearance-none [&::-moz-range-thumb]:w-4 [&::-moz-range-thumb]:h-4 [&::-moz-range-thumb]:rounded-full
      [&::-moz-range-thumb]:transition-colors
      [&::-moz-range-thumb]:border-0
      {active
        ? '[&::-moz-range-thumb]:bg-blue-500 hover:[&::-moz-range-thumb]:bg-blue-600'
        : '[&::-moz-range-thumb]:bg-gray-400 hover:[&::-moz-range-thumb]:bg-gray-500'
      }"
  />
  {#if showValue}
    <input
      type="number"
      {min}
      {max}
      {step}
      bind:value
      {disabled}
      on:input={handleNumberInput}
      class="w-16 px-2 py-1 text-sm border border-gray-300 rounded dark:bg-gray-800 dark:border-gray-700 dark:text-gray-100"
      class:opacity-50={disabled}
    />
    {#if unit}
      <span class="text-sm text-gray-900 dark:text-white" class:opacity-50={disabled}>{unit}</span>
    {/if}
  {/if}
</div>