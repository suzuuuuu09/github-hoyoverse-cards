<script lang="ts">
  import ToggleTheme from "$lib/components/ToggleTheme.svelte";
</script>

<main class="min-h-screen p-8 bg-slate-100 dark:bg-slate-800 transition-all ease-in-out duration-300">
  <div class="max-w-4xl mx-auto">
    <div class="flex justify-end mb-4">
      <ToggleTheme />
    </div>

    <div class="bg-white dark:bg-slate-700 p-8 rounded-lg shadow-lg duration-300">
      <h1 class="text-center">Welcome to Our App</h1>
      
      <div class="space-y-6">
        <section>
          <h2>Button Examples</h2>
          <div class="flex gap-4 mt-2">
            <button class="btn-primary">
              Primary Button
            </button>
            <button class="btn-secondary">
              Secondary Button
            </button>
          </div>
        </section>

        <section>
          <h2>Form Example</h2>
          <div class="space-y-4">
            <div>
              <label for="name" class="label">Name</label>
              <input
                type="text"
                id="name"
                class="input"
                placeholder="Enter your name"
              />
            </div>
            <div>
              <label for="email" class="label">Email</label>
              <input
                type="email"
                id="email"
                class="input"
                placeholder="Enter your email"
              />
            </div>
          </div>
        </section>

        <section>
          <h2>Counter Example</h2>
          <div class="text-center">
          </div>
        </section>
      </div>
    </div>
  </div>
</main>