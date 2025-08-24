def precision_at_k(retrieved, relevant, k):
   
    retrieved_at_k = retrieved[:k]
   
    relevant_count = sum(1 for doc_id in retrieved_at_k if doc_id in relevant)
 
    return relevant_count / k


def reciprocal_rank(retrieved, relevant):
   
    for idx, doc_id in enumerate(retrieved):
        if doc_id in relevant:
            return 1 / (idx + 1)
    return 0


def mean_reciprocal_rank(all_retrieved, all_relevant):
    rr_total = 0
    
    for retrieved, relevant in zip(all_retrieved, all_relevant):
        rr_total += reciprocal_rank(retrieved, relevant)
    return rr_total / len(all_retrieved)



if __name__ == "__main__":
   
    all_retrieved = [
        [
            "1105.4486",
            "1901.07822",
            "2309.07134",
            "1805.08239",
            "2306.04748",
            "1310.0890",
            "2111.14781",
            "2307.02978",
            "2010.08715",
            "2405.00741",
            "2101.05631",
        ],  # Retrieved for Query 1
    ]

    all_relevant = [
        {
            "1105.4486",
            "1901.07822",
            "2309.07134",
            "1805.08239",
            "2306.04748",
            "1310.0890",
            "2111.14781",
            "2307.02978",
            "2010.08715",
            "2405.00741",
            "2101.05631",
            "2501.18671"
        },  # Relevant for Query 1
    ]

   
    print("MRR:", mean_reciprocal_rank(all_retrieved, all_relevant))

  
    k = 12  
    print(f"Precision@{k}:")
    for i in range(len(all_retrieved)):
        p = precision_at_k(all_retrieved[i], all_relevant[i], k)
        print(f"Query {i+1}: {p:.2f}")
