-- Campaigns table schema and sample data for quick provisioning
CREATE TABLE IF NOT EXISTS campaigns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('Active', 'Paused')),
    clicks INTEGER NOT NULL DEFAULT 0,
    cost REAL NOT NULL DEFAULT 0,
    impressions INTEGER NOT NULL DEFAULT 0
);

DELETE FROM campaigns;

INSERT INTO campaigns (id, name, status, clicks, cost, impressions) VALUES
    (1, 'Summer Sale', 'Active', 150, 45.99, 1200),
    (2, 'Black Friday', 'Paused', 320, 89.50, 2500),
    (3, 'New Year Promo', 'Active', 210, 65.00, 1800),
    (4, 'Winter Clearance', 'Paused', 40, 10.00, 400),
    (5, 'Spring Blast', 'Active', 500, 120.00, 5200),
    (6, 'Flash Deal', 'Active', 80, 19.99, 800),
    (7, 'Referral Drive', 'Paused', 30, 5.00, 300),
    (8, 'Holiday Push', 'Active', 240, 70.00, 2200),
    (9, 'Test Campaign 1', 'Paused', 0, 0.00, 0),
    (10, 'Test Campaign 2', 'Active', 10, 2.50, 100);

