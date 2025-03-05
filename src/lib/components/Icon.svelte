<script lang="ts">
  export let path: string;
  export let size: string | number = "24px";
  export let color: string = "currentColor";
  
  let finalSize: string;
  $: {
    finalSize = typeof size === "number" ? `${size}px` : size;
  }
</script>

<svg
  viewBox="0 0 24 24"
  width={finalSize}
  height={finalSize}
  fill={color}
  {...$$restProps}
>
  <path d={path} />
</svg>