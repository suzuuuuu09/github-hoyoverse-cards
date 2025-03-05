export function setCookie(name: string, value: string, days: number = 365) {
  const date = new Date();
  date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
  const expires = `expires=${date.toUTCString()}`;
  document.cookie = `${name}=${value};${expires};path=/`;
}

export function getCookie(name: string): string {
  const nameEQ = `${name}=`;
  const ca = document.cookie.split(';');
  for (const c of ca) {
    const cookie = c.trim();
    if (cookie.startsWith(nameEQ)) return cookie.substring(nameEQ.length);
  }
  return '';
}