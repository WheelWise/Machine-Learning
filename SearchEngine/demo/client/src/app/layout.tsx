import "./globals.css";

export const metadata = {
  title: "Search Engine Demo",
  description: "Just a quick demo and a playground for ML devs ",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
