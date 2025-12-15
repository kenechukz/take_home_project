-- CreateEnum
CREATE TYPE "EventType" AS ENUM ('click', 'page_view', 'form_submit');

-- CreateTable
CREATE TABLE "Interaction" (
    "id" SERIAL NOT NULL,
    "user_id" TEXT NOT NULL,
    "event_type" "EventType" NOT NULL,
    "metadata" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Interaction_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE INDEX "Interaction_user_id_idx" ON "Interaction"("user_id");

-- CreateIndex
CREATE INDEX "Interaction_event_type_idx" ON "Interaction"("event_type");
