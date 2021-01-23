import test_main as tm

def test_is_prime():
  assert not tm.is_prime(1)
  assert tm.is_prime(2)
  assert tm.is_prime(2)
  assert tm.is_prime(3)
  assert not tm.is_prime(4)
  assert tm.is_prime(5)
  assert not tm.is_prime(6)
  assert tm.is_prime(7)
  assert not tm.is_prime(8)
  assert not tm.is_prime(9)
  assert not tm.is_prime(10)
