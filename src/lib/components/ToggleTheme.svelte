<script lang="ts">
  import Icon from '@iconify/svelte'

  let isDark = false
  function toggleTheme() {
    isDark = !isDark
    document.documentElement.classList.toggle('dark')
  }
</script>

<button
  on:click={toggleTheme}
  class="p-3 rounded-lg hover:bg-slate-300 dark:hover:bg-slate-700 duration-300"
>
  <Icon
    icon={isDark ? 'mdi:weather-sunny' : 'mdi:weather-night'}
    class="w-6 h-6 text-slate-900 dark:text-slate-100 duration-300"
  />
</button>