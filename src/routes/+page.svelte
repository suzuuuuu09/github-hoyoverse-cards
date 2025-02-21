<script lang="ts">
  import ThemeToggle from "$lib/components/buttons/ThemeToggleButton.svelte";
  import Card from "$lib/components/Card.svelte";
  import Dropdown from "$lib/components/Dropdown.svelte";
  
  let selectedOption = "Menu";

  function handleSelect(event: CustomEvent<{ selectedOption: string }>) {
    selectedOption = event.detail.selectedOption;
  }
</script>

<main class="min-h-screen p-8 bg-gray-100 dark:bg-gray-900 duration-300">
  <div class="max-w-6xl mx-auto">
    <div class="flex justify-end mb-8">
      <ThemeToggle />
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <Card>
        <h1 class="text-3xl font-bold text-center text-gray-900 dark:text-white duration-300">Card One</h1>
        <Dropdown
          options={["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6", "Option 7", "Option 8", "Option 9", "Option 10", "Option 11", "Option 12", "Option 13", "Option 14", "Option 15", "Option 16", "Option 17", "Option 18", "Option 19", "Option 20", "Option 21", "Option 22", "Option 23", "Option 24", "Option 25", "Option 26", "Option 27", "Option 28", "Option 29", "Option 30"]}
          initialSelectedOption={selectedOption}
          on:select={handleSelect}
        />
      </Card>

      <Card>
        <h1 class="text-3xl font-bold text-center text-gray-900 dark:text-white duration-300">Card Two</h1>
      </Card>
    </div>
  </div>
</main>