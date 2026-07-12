

type Props = {
    title: string;
    data: unknown;
};

function renderValue(value: unknown): React.ReactNode {
    if (value === null || value === undefined) {
        return <p>—</p>;
    }

    if (typeof value === "string") {
        return <p>{value}</p>;
    }

    if (
        typeof value === "number" ||
        typeof value === "boolean"
    ) {
        return <p>{String(value)}</p>;
    }

    if (Array.isArray(value)) {
        return (
            <ul>
                {value.map((item, index) => (
                    <li key={index}>
                        {renderValue(item)}
                    </li>
                ))}
            </ul>
        );
    }

    if (typeof value === "object") {
        return (
            <>
                {Object.entries(value).map(
                    ([key, val]) => (
                        <div
                            key={key}
                            className="result-section"
                        >
                            <h3>
                                {key
                                    .replaceAll("_", " ")
                                    .replace(
                                        /\b\w/g,
                                        (c) =>
                                            c.toUpperCase()
                                    )}
                            </h3>

                            {renderValue(val)}
                        </div>
                    )
                )}
            </>
        );
    }

    return <p>{String(value)}</p>;
}

export default function ResultCard({
    title,
    data,
}: Props) {
    return (
        <div className="result-card">
            <h2>{title}</h2>

            {renderValue(data)}
        </div>
    );
}