CREATE OR REPLACE VIEW vw_dashboard_stats AS 
SELECT
    json_build_object(
        'total_equipments', (SELECT COUNT(*) FROM equipments),
        'total_active_maintenances', (SELECT COUNT(*) FROM maintenances WHERE finished_at IS NULL), 
        'equipment_health_rate', (
            SELECT
                ROUND((COUNT(*) FILTER (WHERE es.name ILIKE '%operacional%')::NUMERIC / NULLIF(COUNT(*), 0) * 100), 1) || '%'
            FROM equipments e
            JOIN equipment_status es ON e.equipment_status_id = es.id
        )
    ) AS summary,
    (
        SELECT json_agg(t)
        FROM (
            SELECT
                e.equipment_status_id AS status,
                COUNT(*) as count
            FROM equipments e
            GROUP BY status
            ORDER BY count DESC
        ) t
    ) AS equipments_by_status,
    (
        SELECT json_agg(t)
        FROM (
            SELECT 
                d.name AS department,
                COUNT(*) AS count
            FROM equipments e
            JOIN departments d ON e.department_id = d.id
            GROUP BY (d.id, d.name)
            ORDER BY count DESC
        ) t
    ) AS equipments_by_department,
    json_build_object(
        'active_count', (SELECT COUNT(*) FROM maintenances WHERE finished_at IS NULL),
        'avg_days_open', (
            SELECT
                COALESCE(AVG(EXTRACT(DAY FROM (NOW() - created_at))), 0) AS avg_days
            FROM maintenances
            WHERE finished_at IS NULL
        ),
        'opened_list', (
            SELECT json_agg(
                json_build_object(
                    'id', m.id,
                    'description', m.description,
                    'created_at', m.created_at,
                    'days_open', EXTRACT(DAY FROM (NOW() - m.created_at)),
                    'responsible', json_build_object(
                        'id', r.id,
                        'full_name', (r.firstname || ' ' || r.lastname),
                        'role', r.role_id
                    )
                )
            )
            FROM maintenances m
            JOIN users r ON m.responsible_id = r.id
            WHERE finished_at IS NULL
        )
    ) AS maintenance_overview
-- (
--     json_build_object(
--         'id', u.id,
--         'full_name', (u.firstname || ' ' || u.lastname),
--         'role', u.role_id
--     )
-- 'responsible_name', r.firstname || ' ' || r.lastname
-- ) ORDER BY EXTRACT(DAY FROM (NOW() - m.created_at)) DESC