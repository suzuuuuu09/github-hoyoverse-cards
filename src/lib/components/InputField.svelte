<script lang="ts">
  export let id: string;
  export let type: string;
  export let placeholder: string;
  export let value = "";
</script>

<input
  {id}
  {type}
  {placeholder}
  bind:value
  class="w-1/2 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-100 duration-300"
/>