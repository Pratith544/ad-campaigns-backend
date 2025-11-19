
CREATE TABLE IF NOT EXISTS campaigns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('Active', 'Paused')),
    clicks INTEGER NOT NULL DEFAULT 0,
    cost REAL NOT NULL DEFAULT 0,
    impressions INTEGER NOT NULL DEFAULT 0,
    image_url TEXT NOT NULL
);

DELETE FROM campaigns;

INSERT INTO campaigns (id, name, status, clicks, cost, impressions, image_url) VALUES
    (1, 'Summer Sale', 'Active', 150, 45.99, 1200, 'https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?auto=format&fit=crop&w=1200&q=80'),
    (2, 'Black Friday', 'Paused', 320, 89.50, 2500, 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80'),
    (3, 'New Year Promo', 'Active', 210, 65.00, 1800, 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80'),
    (4, 'Winter Clearance', 'Paused', 40, 10.00, 400, 'https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d?auto=format&fit=crop&w=1200&q=80'),
    (5, 'Spring Blast', 'Active', 500, 120.00, 5200, 'https://images.unsplash.com/photo-1522199710521-72d69614c702?auto=format&fit=crop&w=1200&q=80'),
    (6, 'Flash Deal', 'Active', 80, 19.99, 800, 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80'),
    (7, 'Referral Drive', 'Paused', 30, 5.00, 300, 'https://images.unsplash.com/photo-1492725764893-90b379c2b6e7?auto=format&fit=crop&w=1200&q=80'),
    (8, 'Holiday Push', 'Active', 240, 70.00, 2200, 'https://images.unsplash.com/photo-1495020689067-958852a7765e?auto=format&fit=crop&w=1200&q=80'),
    (9, 'Test Campaign 1', 'Paused', 0, 0.00, 0, 'https://images.unsplash.com/photo-1487017159836-4e23ece2e4cf?auto=format&fit=crop&w=1200&q=80'),
    (10, 'Test Campaign 2', 'Active', 10, 2.50, 100, 'https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=1200&q=80');

