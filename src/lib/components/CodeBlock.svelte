<script>
  import Icon from "@iconify/svelte";
  import { fade } from 'svelte/transition';

  export let code = '';
  let copied = false;

  async function copyCode() {
    try {
      await navigator.clipboard.writeText(code);
      copied = true;
      setTimeout(() => {
        copied = false;
      }, 2000);
    } catch (err) {
      console.error('Failed to copy code:', err);
    }
  }
</script>

<div class="relative rounded-lg bg-gray-900 px-4 py-3">
  <div class="absolute right-2 top-2 flex items-center gap-2">
    {#if copied}
      <span class="text-sm text-gray-300 bg-gray-700 px-2 py-1 rounded" transition:fade>
        Copied!
      </span>
    {/if}
    <button
      on:click={copyCode}
      class="rounded p-1.5 bg-gray-700 text-gray-300 transition-colors hover:bg-gray-600"
      title="Copy code"
    >
      <Icon icon={copied ? 'mdi:check' : 'mdi:content-copy'} class="w-5 h-5" />
    </button>
  </div>
  
  <pre class="flex overflow-x-auto pt-8">
    <code class="block w-full font-mono text-sm text-gray-300">{code}</code>
  </pre>
</div>