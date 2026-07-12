interface StatusBadgeProps {
    status: string;
}

export default function StatusBadge({
    status,
}: StatusBadgeProps) {
    const normalized = status.toLowerCase();

    let color = "#6b7280";
    let icon = "⚪";

    switch (normalized) {
        case "pending":
            color = "#f59e0b";
            icon = "🟡";
            break;

        case "running":
            color = "#3b82f6";
            icon = "🔵";
            break;

        case "completed":
            color = "#10b981";
            icon = "🟢";
            break;

        case "failed":
            color = "#ef4444";
            icon = "🔴";
            break;
    }

    return (
        <span
            style={{
                display: "inline-flex",
                alignItems: "center",
                gap: "6px",
                padding: "6px 12px",
                borderRadius: "999px",
                backgroundColor: `${color}20`,
                color,
                fontWeight: 600,
                fontSize: "14px",
            }}
        >
            <span>{icon}</span>
            {status}
        </span>
    );
}