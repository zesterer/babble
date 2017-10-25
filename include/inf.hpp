#include <gmp.h>
#include <string>
#include <cstdint>

struct inf
{
	mpz_t i;
	
	inf() { mpz_init(this->i); }
	inf(intmax_t i) { mpz_init_set_si(this->i, i); }
	inf(const inf& i) { mpz_init(this->i); mpz_set(this->i, i.i); }
	inf(inf& i) { mpz_init(this->i); mpz_set(this->i, i.i); }
	inf(std::string s, int base = 10) { mpz_init(this->i); this->set(s, base); }
	
	~inf()
	{
		mpz_clear(this->i);
	}
	
	inf& operator=(inf i) { mpz_set(this->i, i.i); return *this; }
	
	inf& operator+=(inf i) { mpz_add(this->i, this->i, i.i); return *this; }
	inf& operator-=(inf i) { mpz_sub(this->i, this->i, i.i); return *this; }
	inf& operator*=(inf i) { mpz_mul(this->i, this->i, i.i); return *this; }
	inf& operator/=(inf i) { mpz_fdiv_q(this->i, this->i, i.i); return *this; }
	inf& operator%=(inf i) { mpz_fdiv_r(this->i, this->i, i.i); return *this; }
	
	intmax_t num() { return mpz_get_ui(this->i); }
	
	std::string str(int base = 10)
	{
		char buff[8192];
		mpz_get_str(buff, base, this->i);
		return std::string(buff);
	}
	
	inf& set(std::string str, int base = 10)
	{
		mpz_set_str(this->i, str.c_str(), base);
		return *this;
	}
	
	inf pow(intmax_t i)
	{
		inf n;
		mpz_pow_ui(n.i, this->i, i);
		return n;
	}
};

inf operator+(inf a, inf b) { inf n; mpz_add(n.i, a.i, b.i); return n; }
inf operator-(inf a, inf b) { inf n; mpz_sub(n.i, a.i, b.i); return n; }
inf operator*(inf a, inf b) { inf n; mpz_mul(n.i, a.i, b.i); return n; }
inf operator/(inf a, inf b) { inf n; mpz_fdiv_q(n.i, a.i, b.i); return n; }
inf operator%(inf a, inf b) { inf n; mpz_fdiv_r(n.i, a.i, b.i); return n; }
