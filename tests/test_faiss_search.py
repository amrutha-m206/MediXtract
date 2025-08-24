from backend.app import perform_search


# Test for search results from FAISS
def test_faiss_returns_results():
    results = perform_search("parkinsons")
    assert isinstance(results, list)  
    assert len(results) > 0  
    assert "title" in results[0]  


# Test for valid structure of each result
def test_valid_result_structure():
    results = perform_search("brain tumor")
    assert isinstance(results, list)
    assert len(results) > 0
    for result in results:
        assert "title" in result
    
