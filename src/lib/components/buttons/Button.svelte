<script lang="ts">
  export let variant: 'default' | 'secondary' | 'destructive' | 'outline' = 'default';
  export let size: 'sm' | 'default' | 'lg' = 'default';
  export let type: 'button' | 'submit' | 'reset' = 'button';
</script>

<button
  {type}
  on:click
  class="inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 {
    variant === 'default' ? 'bg-blue-600 text-white hover:bg-blue-700' :
    variant === 'secondary' ? 'bg-gray-100 text-gray-900 hover:bg-gray-200 dark:bg-gray-700 dark:text-gray-100 dark:hover:bg-gray-600' :
    variant === 'destructive' ? 'bg-red-600 text-white hover:bg-red-700' :
    'border border-gray-200 bg-white hover:bg-gray-100 hover:text-gray-900 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700 dark:hover:text-gray-100'
  } {
    size === 'sm' ? 'h-9 px-3' :
    size === 'lg' ? 'h-11 px-8' :
    'h-10 px-4 py-2'
  }"
>
  <slot />
</button>