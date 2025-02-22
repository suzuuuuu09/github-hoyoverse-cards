<script lang="ts">
  import Icon from '@iconify/svelte'

  let isDark = false;
  let isAnimating = false;

  function toggleTheme() {
    isAnimating = true;
    isDark = !isDark;
    document.documentElement.classList.toggle('dark');
    
    setTimeout(() => {
      isAnimating = false;
    }, 300);
  }
</script>

<button
  on:click={toggleTheme}
  class="p-3 rounded-lg hover:bg-slate-300 dark:hover:bg-slate-700 duration-300 relative w-12 h-12"
>
  <div class="absolute inset-0 flex items-center justify-center">
    {#if isDark}
      <div class="flex items-center justify-center" 
           class:rotate-enter={isAnimating}>
        <Icon icon="mdi:weather-sunny" 
              class="text-2xl text-slate-300 duration-300"/>
      </div>
    {:else}
      <div class="flex items-center justify-center"
           class:rotate-exit={isAnimating}>
        <Icon icon="mdi:weather-night" 
              class="text-2xl text-slate-700 duration-300"/>
      </div>
    {/if}
  </div>
</button>

<style>
  .rotate-enter {
    animation: rotateRight 0.3s ease-in-out;
  }

  .rotate-exit {
    animation: rotateLeft 0.3s ease-in-out;
  }

  @keyframes rotateRight {
    from {
      transform: rotate(-180deg);
      opacity: 0;
    }
    to {
      transform: rotate(0);
      opacity: 1;
    }
  }

  @keyframes rotateLeft {
    from {
      transform: rotate(180deg);
      opacity: 0;
    }
    to {
      transform: rotate(0);
      opacity: 1;
    }
  }
</style>