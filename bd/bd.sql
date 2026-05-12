
-- 1. TABLAS MAESTRAS (Con campos de auditoría exigidos)
-- ==========================================

CREATE TABLE "statusTypes" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    context VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

CREATE TABLE "currencies" (
    id CHAR(3) PRIMARY KEY, -- Mantenemos el código como ID por el estándar ISO
    symbol VARCHAR(5) NOT NULL,
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

CREATE TABLE "services" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    isCustom BOOLEAN DEFAULT FALSE,
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

-- ==========================================
-- 2. NÚCLEO DE USUARIOS
-- ==========================================

CREATE TABLE "users" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100),
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

-- ==========================================
-- 3. SUSCRIPCIONES Y CLASIFICACIÓN
-- ==========================================

CREATE TABLE "categories" (
    id SERIAL PRIMARY KEY,
    user_id UUID REFERENCES "users"(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

CREATE TABLE "subscriptions" (
    id SERIAL PRIMARY KEY,
    user_id UUID REFERENCES "users"(id) ON DELETE CASCADE,
    service_id INT REFERENCES "services"(id),
    category_id INT REFERENCES "categories"(id) ON DELETE SET NULL,
    currency_id CHAR(3) REFERENCES "currencies"(id),
    amount DECIMAL(10, 2) NOT NULL,
    billingCycle VARCHAR(50) NOT NULL,
    nextBillingDate DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

-- ==========================================
-- 4. HISTORIAL Y AUDITORÍA
-- ==========================================

CREATE TABLE "paymentHistories" (
    id BIGSERIAL PRIMARY KEY,
    subscription_id INT REFERENCES "subscriptions"(id) ON DELETE CASCADE,
    amountPaid DECIMAL(10, 2) NOT NULL,
    paymentDate TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

CREATE TABLE "priceHistories" (
    id SERIAL PRIMARY KEY,
    subscription_id INT REFERENCES "subscriptions"(id) ON DELETE CASCADE,
    price DECIMAL(10, 2) NOT NULL,
    effectiveFrom DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

-- ==========================================
-- 5. COMPARTICIÓN (M:N Ordenada Alfabéticamente) Y DEUDAS
-- ==========================================

-- Antes era subscriptionShares, ahora cumple la regla N:M (subscriptions + users)
CREATE TABLE "subscriptions_users" (
    id SERIAL PRIMARY KEY,
    subscription_id INT REFERENCES "subscriptions"(id) ON DELETE CASCADE,
    user_id UUID REFERENCES "users"(id) ON DELETE CASCADE,
    percentage DECIMAL(5, 2) NOT NULL CHECK (percentage > 0 AND percentage <= 100),
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

CREATE TABLE "debts" (
    id SERIAL PRIMARY KEY,
    subscriptions_user_id INT REFERENCES "subscriptions_users"(id) ON DELETE CASCADE,
    amountOwed DECIMAL(10, 2) NOT NULL,
    isPaid BOOLEAN DEFAULT FALSE,
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

-- ==========================================
-- 6. NOTIFICACIONES
-- ==========================================

CREATE TABLE "notificationConfigs" (
    id SERIAL PRIMARY KEY,
    subscription_id INT REFERENCES "subscriptions"(id) ON DELETE CASCADE,
    channel VARCHAR(50) NOT NULL,
    leadTimeDays INT NOT NULL,
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

CREATE TABLE "notificationLogs" (
    id BIGSERIAL PRIMARY KEY,
    notificationConfig_id INT REFERENCES "notificationConfigs"(id) ON DELETE CASCADE,
    sentAt TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    resultStatus VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'Active',
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_id UUID,
    modified_id UUID
);

-- ==========================================
-- 7. SEGURIDAD (RLS SUPABASE)
-- ==========================================

ALTER TABLE "subscriptions" ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Usuarios ven sus propias suscripciones" 
ON "subscriptions" FOR ALL 
USING (auth.uid() = user_id);