import { z } from "zod";

export const FeatureRequestSchema = z.object({
  id: z.number().int(),
  title: z.string(),
  description: z.string().max(150),
  created_at: z.string().date(),
  rating: z.number().int().nullable()
});

export type FeatureRequest = z.infer<typeof FeatureRequestSchema>;

export const FeatureRequestPostSchema = z.object({
  title: z.string().min(1).max(10),
  description: z.string().min(1).max(255),
});

export type FeatureRequestPost = z.infer<typeof FeatureRequestPostSchema>;
