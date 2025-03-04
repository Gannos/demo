import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { z } from 'zod';
import { FeatureRequestSchema } from "$lib/types";
//import { featureRequests } from '$lib/stores/featureRequestStore';
import { get } from 'svelte/store';
import type { PageServerLoad } from './$types';

const API_URL = import.meta.env.VITE_API_URL;

export const load: PageServerLoad = async() => {
    const result = await fetch(`${API_URL}/api/feature_request`);
    if (!result.ok) {
        throw new Error("Failed fetch feature requests");
    }
    const data = await result.json();
    const parsed = z.array(FeatureRequestSchema).safeParse(data);

    if (!parsed.success) {
        console.log("validation failed", parsed.error);
        return { featureRequests: [] };
    }
    console.log("parsed: ", parsed.data);
    //featureRequests.set(parsed.data);
    return { featureRequests: parsed.data.sort((a, b) => b.rating - a.rating) };
};
