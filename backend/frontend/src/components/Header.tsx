import { Link } from "react-router-dom";

export default function Header() {
    return (
        <header className="header">
            <div className="header-content">

                <Link
                    to="/"
                    className="logo"
                >
                    🚀 FounderAI
                </Link>

                <nav className="nav">
                    <Link to="/">Home</Link>

                    <Link to="/dashboard">
                        Dashboard
                    </Link>
                </nav>

            </div>
        </header>
    );
}