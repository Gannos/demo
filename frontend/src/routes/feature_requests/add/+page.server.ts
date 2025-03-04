import { superValidate } from 'sveltekit-superforms';
import { message } from 'sveltekit-superforms';
import { fail, redirect, error } from '@sveltejs/kit';
import { zod } from 'sveltekit-superforms/adapters';
import { z } from 'zod';
import { FeatureRequestPostSchema } from "$lib/types";
import type { Actions } from "./$types";

export const load = async () => {
  const form = await superValidate(zod(FeatureRequestPostSchema));
  return { form };
};

export const actions = {
  default: async({ request }) => {
    const form = await superValidate(request, zod(FeatureRequestPostSchema));
    console.log("form: ", form);
    if (!form.valid) {
      return fail(400, { form });
    }
    const response = await fetch("http://nginx:80/api/feature_request/add", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form.data)
    });

    if (!response.ok) {
      return fail(500, { form, error: "Failed to submit request" });
    }
    message(form, "Form posted successfully");
    throw redirect(303, "/feature_requests");
  }
} satisfies Actions;
