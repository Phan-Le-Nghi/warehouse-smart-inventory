export type LocationOption = {
  id: string
  code: 'BACKROOM' | 'SALES_SHELF'
}

export type PutawayContext = {
  receive_line_id: string
  sku_id: string
  sku: string
  actual_quantity: number
  confirmed_quantity: number
  eligible_quantity: number
  locations: LocationOption[]
}

export type PutawayResult = {
  putaway_id: string
  receive_line_id: string
  sku_id: string
  quantity: number
  destination_location_id: string
  destination_location: string
  confirmed_at: string
  stock: {
    destination_quantity: number
    warehouse_total: number
  }
}

type ErrorEnvelope = {
  error?: {
    code?: string
    message?: string
  }
}

const apiBaseUrl = (import.meta.env.VITE_API_BASE_URL ?? '').replace(/\/$/, '')

async function parseResponse<T>(response: Response): Promise<T> {
  const body = (await response.json()) as T & ErrorEnvelope
  if (!response.ok) {
    throw new Error(body.error?.message ?? 'The request could not be completed.')
  }
  return body
}

export async function loadPutawayContext(
  receiveLineId: string,
): Promise<PutawayContext> {
  const response = await fetch(
    `${apiBaseUrl}/api/v1/putaways/context/${receiveLineId}`,
  )
  return parseResponse<PutawayContext>(response)
}

export async function submitPutaway(
  context: PutawayContext,
  destinationLocationId: string,
  idempotencyKey: string,
): Promise<PutawayResult> {
  const response = await fetch(`${apiBaseUrl}/api/v1/putaways`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Idempotency-Key': idempotencyKey,
    },
    body: JSON.stringify({
      receive_line_id: context.receive_line_id,
      sku_id: context.sku_id,
      quantity: context.eligible_quantity,
      destination_location_id: destinationLocationId,
    }),
  })
  return parseResponse<PutawayResult>(response)
}
