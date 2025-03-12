<script lang="ts">
  export let id: string;
  export let type: string;
  export let placeholder: string;
  export let value = "";
  export let min: number | undefined = undefined;
  export let max: number | undefined = undefined;

  function handleInput(event: Event) {
    if (type === "number") {
      const input = event.target as HTMLInputElement;
      const num = Number(input.value);
      
      if (!isNaN(num)) {
        if (min !== undefined && num < min) {
          value = String(min);
        } else if (max !== undefined && num > max) {
          value = String(max);
        } else {
          value = input.value;
        }
      }
    }
  }
</script>

<input
  {id}
  {type}
  {placeholder}
  bind:value
  min={type === "number" ? min : undefined}
  max={type === "number" ? max : undefined}
  on:input={handleInput}
  class="w-1/2 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-100 duration-300"
/>