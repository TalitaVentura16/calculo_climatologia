program clima 

    character(10) :: xxx, yyy ! nomes dos arquivos

    read(10, file = xxx) pentada
    read(20, file = yyy) pentclim

    integer :: NY, NP, i, j


    do k = 1, NY
        icont_i = 0
        icont_f = 0
        do i = 1, NP ! (número de pentadas total 365 / 5)
            do j = i, i+8
                if (pentada(i). lt. pentclim(i)) icont_i = icont_i + 1
                if (pentada(i).gt.pentclim(i)) icont_f = icont_f + 1
            enddo
            if(icont_i.ge.6) then
                kpi = k * i
                write(20,*) k, i, kpi(k)
            endif
            if(icont_f.ge.6)then
                kpf = k * i
                write(30,*) k, i, kpf(k)
            endif
        enddo

        do k = 1, NY
            dsl = kpf (k) - kpi (k)
            write (40,*) k, dsl
        enddo
    enddo

end program clima