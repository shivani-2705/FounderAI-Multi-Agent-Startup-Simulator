import type { ReactNode } from "react";

import Header from "../components/Header";

interface Props {
    children: ReactNode;
}

export default function MainLayout({
    children,
}: Props) {
    return (
        <>
            <Header />

            <main className="container">
                {children}
            </main>
        </>
    );
}