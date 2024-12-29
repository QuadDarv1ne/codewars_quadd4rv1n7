function hello(name) {
  if (!name) {
    return "Hello, World!";
  }
  // Capitalize the first letter and lowercase the rest of the name
  return `Hello, ${name.charAt(0).toUpperCase() + name.slice(1).toLowerCase()}!`;
}
