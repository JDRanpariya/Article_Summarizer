import { useEffect, useState } from "react";

export default function ThemeToggle() {
  const [dark, setDark] = useState(false);

  useEffect(() => {
    if (dark) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, [dark]);

  return (
    <button
      onClick={() => setDark(!dark)}
      className="fixed top-4 right-4 px-3 py-1 bg-brand text-white dark:bg-gray-800 rounded"
    >
      {dark ? "🌙 Dark" : "☀️ Light"}
    </button>
  );
}

